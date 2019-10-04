#lang racket

(require xml)
(define (load-xexpr path)
  (xml->xexpr (document-element (read-xml (open-input-file path)))))

(require explorer)
(define data (load-xexpr "rubrics.xml"))
(explore data)

(define (load-rubrics file-name)
  (list-tail (load-xexpr file-name) 2)) ; remove first two elements of the list

(module+ test
  (require rackunit)
  (define rubrics (load-rubrics  "rubrics.xml"))
  (check-equal? (length rubrics) 5)
  (for ([elt rubrics])
    (check-equal? (first elt) 'rubric)))