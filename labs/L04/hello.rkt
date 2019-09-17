(module hello racket
  (provide hello)
  (define (hello)
    (displayln "Hello world!"))

  (module+ test
    (require rackunit)
    (check-equal? (with-output-to-string hello) "Hello world!\n")
    (check-equal? (with-output-to-string hello) (begin (sleep 3) "Hello world!\n")))

  (module* main #f
    (hello)))