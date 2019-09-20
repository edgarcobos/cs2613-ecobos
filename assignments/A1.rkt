#lang racket

(define (drop-divisible i list)
  (define (drop num)
    (cond
      [(equal? num i) #f]
      [(zero? (remainder num i)) #t]
      [else #f]))
  (remv* (filter drop list) list))

(module+ test
  (require rackunit)
  (check-equal? (drop-divisible 3 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 7 8 10))
  (check-equal? (drop-divisible 3 (list 5 9 14 11 12 13 24 36 5 6 9 36 10 11)) (list 5 14 11 13 5 10 11)))

(define (sieve-with divlist list)
  (cond
    ((empty? divlist) list)
    (else (drop-divisible (first divlist) (sieve-with (rest divlist) list)))))

(module+ test
  (check-equal? (sieve-with '(2 3) (list 2 3 4 5 6 7 8 9 10)) (list 2 3 5 7))
  (check-equal? (sieve-with '(2 3 5) (list 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25)) (list 2 3 5 7 11 13 17 19 23)))

(define (sieve n)
  (sieve-with (range 2 (add1 (sqrt n))) (range 2 (add1 n))))

(module+ test
  (check-equal? (sieve 10) (list 2 3 5 7))
  (check-equal? (sieve 21) (list 2 3 5 7 11 13 17 19)))

(module+ test
  (require math/number-theory)
  (check-equal? (sieve 10) (filter prime? (range 2 10)))
  (check-equal? (sieve 12) (filter prime? (range 2 12)))
  (check-equal? (sieve 500) (filter prime? (range 2 500))))