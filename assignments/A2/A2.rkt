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

(define (assoc-all value list)
  (define (helper list)             ; navigate through sublists
    (cond
      [(empty? list) '()]           ; if the list is empty then return empty list
      [(equal? (first list) value)  ; first element of the list is the value
            list]                   ; return the list
      [(list? (first list))         ; else if the first element of the list is a list
       (helper (first list))]       ; look for value in list
      [else (helper (rest list))])) ; else look into rest of list for value
 
  (define (assoc value list)
    (cond
      [(empty? list) '()]                                          ; if value was not found return null
      [(list? (first list))                                        ; first element of list is a list
       (cons (helper (first list)) (assoc value (rest list)))]     ; call helper to find all occurances of value
      [else (assoc value (rest list))]))                           ; else return recursive call with rest of list
  (check-empty (assoc value list)))                                ; check if all sublists are empty

(define (check-empty lst)
  (cond              
    [(empty? lst) '()]                            ; if list is empty return empty list
    [(empty?(first lst)) (check-empty (cdr lst))] ; if first element of list is empty return recursive call with second element
    [else lst]))                                  ; else return lst

(module+ test
  (check-equal? (assoc-all 'keep test-list) '([keep 2] [keep 4] [keep 5]))
  (check-equal? (assoc-all 'discard test-list) '()))