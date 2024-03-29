function ratio=knn2(k,training, testing, output=0)

  correct = 0;
  for i=1:rows(testing)
    row=testing(i,:);
    if findclass(row,k,training,@nearest2) == row(1);
      correct += 1;
    endif
  endfor

  ratio = correct/rows(testing);
endfunction