#lang racket

(define (binmap op lst lst2)
  (cond
    [(or (empty? lst) (empty? lst2)) empty]
    [else (cons (op (first lst) (first lst2))
          (binmap op (rest lst) (rest lst2)))]))

(module+ test
  (require rackunit)

  (check-equal? (binmap + '(1 2 3) '(4 5 6)) '(5 7 9))
  (check-equal? (binmap * '(1 2 3) '(4 5 6)) '(4 10 18))

  (check-equal? (binmap string-append '("hello" "world ")
                                      '(" mom" "travel"))
        '("hello mom" "world travel"))

  (check-equal? (binmap + '(1 2 3) '(4 5 6 7)) '(5 7 9))
  (check-equal? (binmap + '(1 2 3 4) '(4 5 6)) '(5 7 9)))