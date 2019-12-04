function out = nearest(v, k, data)
  for i=1:rows(data)
    dist(i)=norm(v(2:end)-data(i,2:end));
  endfor
  [sorted, indices]=sort(dist);
  indices(1:k)
  out = sort(indices(1:k));
endfunction

%!test
%! v = [0,1,1]
%! data = [0,0,0; 0,0,1; 0,1,0; 1,1,1]
%! assert(nearest(v,1,data) == 4)
%! assert(nearest(v,3,data) == [2,3,4])