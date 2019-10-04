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

(define (assoc* value list)
  (cond
    [(empty? list) #f]                                                  ; if list is empty return false
    [(and (and (list? (first list)) (not (list? (first (first list))))) ; first element is a list and first element of first list is not a list
     (equal? (first (first list)) value))                               ; first element of first list is value
             (second (first list))]                                     ; return value that corresponds to key
    [else (assoc* value (rest list))]))                                 ; else return recursive call with rest of list

(module+ test
  (define test-list '(1 [keep 2] 3 [keep 4] [keep 5] 6))
  (check-equal? (assoc* 'keep test-list) 2)
  (check-equal? (assoc* 'discard test-list) #f))

(define (rubric-name rubric)
  (assoc* 'name (second rubric)))

(module+ test
  (check-equal?
   (sort (map rubric-name rubrics) string<=?)
   '("JavaScript Assignment" "Journal Entry" "Octave Assignment" "Python Assignment"
                             "Racket assignment")))