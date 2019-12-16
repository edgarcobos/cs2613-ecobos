#lang racket

(define (sixes-and-sevens lst)
  (define (helper lst acc)
    (cond
      [(empty? lst) acc]
      [(zero? (remainder (first lst) 6)) (helper (rest lst) (cons (first lst) acc))]
      [(zero? (remainder (first lst) 7)) (helper (rest lst) (cons (first lst) acc))]
      [else (helper (rest lst) acc)]))
  (reverse (helper lst '())))

(module+ test
  (require rackunit)
  ;; empty list
  (check-equal? (sixes-and-sevens '()) '())
  ;; ascending order + all multiples of 6 and 7
  (check-equal? (sixes-and-sevens '(6 7 12 14)) '(6 7 12 14))
  ;; descending order + one (non-multiple of zero) + zero (multiple of zero)
  (check-equal? (sixes-and-sevens '(14 12 1 0)) '(14 12 0)))