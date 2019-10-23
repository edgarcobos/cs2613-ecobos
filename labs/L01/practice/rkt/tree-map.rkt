#lang racket

(define (tree-map func lst)
  (cond
    [(empty? lst) lst]
    [(list? (first lst)) (cons (cons (func (first (first lst)))
                                           (tree-map func (rest (first lst)))) (tree-map func (rest lst)))]
    [else (cons (func (first lst))
                (tree-map func (rest lst)))]))

(module+ test
  (require rackunit)
  (check-equal? (tree-map add1 '()) '())
  (check-equal? (tree-map add1 '(1 2 3)) '(2 3 4))
  (check-equal? (tree-map (lambda (x) (* x x)) '(1 2 3)) '(1 4 9))
  (check-equal? (tree-map sub1 '(1 (2 3))) '(0 (1 2)))
  (check-equal? (tree-map (lambda (x) (modulo x 2))
                          '((1 2) (3 4) 5 (6 (7))))
                '((1 0) (1 0) 1 (0 (1))))
  (check-equal? (tree-map (lambda (x)
                            (string-append "I wanna " x))
                          '("pony" ("xbox" "A+")))
'("I wanna pony" ("I wanna xbox" "I wanna A+"))))