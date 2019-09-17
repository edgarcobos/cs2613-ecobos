 #lang racket
    (define (fact n)
      (cond
        [(zero? n) 1]
        [else (* (fact (sub1 n)) n)]))

    (module+ test
      (require rackunit)
      (check-equal? (fact 10) 3628800))