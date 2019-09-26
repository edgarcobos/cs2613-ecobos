#lang racket
(require (for-syntax racket/match))
(require (for-syntax "let-transformer.rkt"))

(define-syntax (Let* stx)
  (datum->syntax #'here
                 (let-transformer
                  (syntax->datum stx))))

(define-syntax (Let^ stx)
  (syntax-case stx ()
    [(Let^ () body) #'body]
    [(Let^ ((first-id first-val) (id val) ...) body)
     #'(let ([first-id first-val])
         (Let^ [(id val) ...] body))]))

(module+ test
  (require rackunit)
  (check-equal? (Let^ ([x 5] [y (- x 3)]) (+ y y)) 4)
  (check-equal? (Let^ ([x 5] [y (- x 3)] [y x]) (* y y)) 25))