## usage: given a matrix of integers, for each row
## return the column containing the minimum value
function out = mincol(data)
  [r, out] = min(data,[],2);
endfunction
%!test
%! A = [1,2,3;
%!     3,2,4;
%!     1,2,0;
%!     5,3,4;
%!     3,2,1;
%!     -10,0,0];
%! assert (mincol(A) == [1;2;3;2;3;1]);