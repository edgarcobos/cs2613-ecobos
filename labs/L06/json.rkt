#lang racket
(require explorer)
(require json)

(define (read-json-file file-name)
  (with-input-from-file file-name read-json))

(define (visualize-json-file file-name)
  (explore (read-json-file file-name)))

(define (visualize)
  (visualize-json-file "erorrs.json"))

(define (collect-one-status hash-table)
  (hash-ref hash-table 'status))

(module+ test
  (require rackunit)
  (define test-JSON (read-json-file "errors.json")

  (check-equal?
   (collect-one-status (first (hash-ref JSON 'errors))) "403")))

(define (collect-status file-name)
  (define (json read-json-file "errors.json"))
  (map collect-one-status (first (has-ref test-JSON 'errors)))

(module+ test
  (require rackunit)
  (check-equal? (collect-status "errors.json") '("403" "422" "500")))

(define (collect-status2 filename)
  (define (helper in-lst acc)
    (cond
      [(empty? in-lst) acc]
      [else (helper (rest in-lst) (cons (collect-one-status (first in-lst)) acc))]))
  (helper (hash-ref (read-json-file filename) 'errors) '()))

(module+ test
  (check-equal? (sort (collect-status "errors.json") string<?)
                (sort (collect-status2 "errors.json") string<?)))

(collect-status2 "errors.json")