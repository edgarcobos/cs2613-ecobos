#lang racket

(define (list->hash lst hash i)
  (cond
    [(empty? lst) hash]
    [else (list->hash (rest lst) (hash-set hash i (first lst)) (add1 i))]))

(module+ test
  (require rackunit)
  (define hash-table (list->hash (list "a" "b" "c") (hash) 1))
  (check-equal? (hash-ref hash-table 1) "a")
  (check-equal? (hash-ref hash-table 2) "b")
  (check-equal? (hash-ref hash-table 3) "c"))