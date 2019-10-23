#lang racket
(define (sum-pos . nums)
  (define (sum-pos-helper nums acc)
    (cond
      [(empty? nums) acc]
      [(positive? (first nums)) (sum-pos-helper (rest nums) (+ acc (first nums)))]
      [else (sum-pos-helper (rest nums) acc)]))
  (sum-pos-helper nums 0))



(module+ test
  (require rackunit)
  (check-equal? (sum-pos) 0)
  (check-equal? (sum-pos 1) 1)
  (check-equal? (sum-pos 1 0 -1) 1)
  (check-equal? (apply sum-pos (range -9 10)) 45))
