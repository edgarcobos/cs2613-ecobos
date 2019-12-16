#lang racket

(define (binmap op lst lst2)
  (define (helper lst lst2 acc)
    (cond
      [(or (empty? lst) (empty? lst2)) acc]
      [else (helper (rest lst) (rest lst2) (cons (op (first lst) (first lst2)) acc))]))
  (reverse (helper lst lst2 '())))

(module+ test
  (require rackunit)

  (check-equal? (binmap + '(1 2 3) '(4 5 6)) '(5 7 9))
  (check-equal? (binmap * '(1 2 3) '(4 5 6)) '(4 10 18))

  (check-equal? (binmap string-append '("hello" "world ")
                                      '(" mom" "travel"))
        '("hello mom" "world travel"))

  (check-equal? (binmap + '(1 2 3) '(4 5 6 7)) '(5 7 9))
  (check-equal? (binmap + '(1 2 3 4) '(4 5 6)) '(5 7 9)))