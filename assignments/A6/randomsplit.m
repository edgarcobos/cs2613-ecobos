## usage: randomsplit(array, ratio)
##
## split the rows of a matrix randomly in the given ratio

function [foo, bar] = randomsplit(matrix, ratio)
  [x,y] = size(matrix);
  ratioM = x*ratio;                               %compute ratio with number of rows
  idx = randperm(x);
  foo = matrix(idx(1:ratioM),:);          %upper array
  bar = matrix(idx(ratioM+1:end),:); %lower array
endfunction

%!assert(randomsplit(zeros(10,1), 0.5) == [zeros(5,1),zeros(5,1)])

%!test
%! [foo, bar] = randomsplit(zeros(10,1), 0.7);
%! assert(foo == zeros(7,1))
%! assert(bar == zeros(3,1))

%!test
%! [foo, bar] = randomsplit(2*ones(4,2), 0.5);
%! assert(foo == 2*ones(2,1))
%! assert(bar == 2*ones(2,1))