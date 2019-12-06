## usage: tally(matrix)
##
## returns the column with the most votes, or c+1 if no column has votes

function c = tally(matrix)
  [r,c] = max(matrix,[],2);         %arbitrary c with the most votes
  idx = find(r == 0);                   %if no column has votes
  c(idx) = columns(matrix) + 1; %c+1
endfunction

%!test
%! A = [1,2,3;
%!     2,1,3;
%!     2,3,1;
%!     3,1,2;
%!     3,2,1;
%!     0,0,0];
%! assert (tally(A) == [3;3;2;1;1;4]);

%!test
%! A = [0,0,0;
%!     1,2,3;
%!     2,1,3;
%!     0,1,3;
%!     3,2,0;
%!     0,0,0];
%! assert (tally(A) == [4;3;3;3;1;4]);