function out = nearest2(v, k, data)

  diff = data(:,2:end) - ones(rows(data),1)*v(2:end);
  normsq = dot(diff,diff,2)
  [sorted, indices]=sort(normsq);
  out = sort(transpose(indices(1:k)));
endfunction

%!test
%! v = [0,1,1];
%! data = [0,0,0; 0,0,1; 0,1,0; 1,1,1];
%! assert(nearest2(v,1,data) == 4)
%! assert(nearest2(v,3,data) == [2,3,4])