## usage: ranges(array)
##
## returns a matrix of the max and min values for each coordinate in a matrix

function res = ranges(matrix)
  res = [min(matrix);max(matrix)];
endfunction

%!test
%! A=[0,0,0;
%!    0,1,0;
%!    0,0,1;
%!    1,1,1];
%! assert (ranges(A), [0,0,0;
%!                     1,1,1]);

%!test
%! A=[0,0,0;
%!    0,10,0;
%!    0,0,1;
%!    1,1,-11];
%! assert (ranges(A), [0,0,-11;
%!                     1,10,1]);

%!test
%! A=[4,5,6;
%!    1,8,9;
%!    7,2,3];
%! assert (ranges(A), [1,2,3;
%!                     7,8,9]);