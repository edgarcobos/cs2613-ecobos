#lang racket
(define (tr-length list)
  (define (helper lst acc)
    (cond
      [(empty? lst) acc]
      [(helper (rest lst) (add1 acc))]))
  (helper list 0))

(define abc (list "a" "b" "c"))
(define abclong (list "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l"))

(module+ test
  (require rackunit)
  (check-equal? (tr-length abc) 3)
(check-equal? (tr-length abclong) 12))