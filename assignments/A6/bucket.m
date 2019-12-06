## usage: bucket(v, ranges, p)
##
## calculates which of the pᶠ boxes a given vector is in

function res = bucket(v, ranges, p)
  w = (ranges(2,:)-ranges(1,:))/p;
  res = floor((v-ranges(1,:))./w)(2:end);
  res(res > p-1) = p-1;
endfunction

%!test "[*,0] -> bucket 0"
%!shared zero_one
%! zero_one=[0,0;1,1];
%! assert(bucket([0,0],zero_one,2) == 0)
%! assert(bucket([1,0],zero_one,2) == 0)

%!test "[*,0.1] -> bucket 0"
%!shared zero_one
%! zero_one=[0,0;1,1];
%! assert(bucket([0,0.1],zero_one,2) == 0)
%! assert(bucket([1,0.1],zero_one,2) == 0)

%!test "[*,0.5] -> bucket 1"
%! assert(bucket([0,0.5],zero_one,2) == 1)
%! assert(bucket([1,0.5],zero_one,2) == 1)

%!test "[*,0.6] -> bucket 1"
%! assert(bucket([0,0.6],zero_one,2) == 1)
%! assert(bucket([1,0.6],zero_one,2) == 1)

%!test "[*,1] -> bucket 1"
%! assert(bucket([0,1],zero_one,2) == 1)
%! assert(bucket([1,1],zero_one,2) == 1)

%!test "[*,1] p=3 -> bucket 2"
%! assert(bucket([0,1],zero_one,3) == 2)
%! assert(bucket([1,1],zero_one,3) == 2)

%!test "[*,1] (range=1,2) -> bucket 0"
%!shared one_two
%! one_two=[1,1;2,2];
%! assert(bucket([0,1],one_two,2) == 0)
%! assert(bucket([1,1],one_two,2) == 0)

%!test "[*,1.5] (range=1,2, p=3) -> bucket 1"
%! assert(bucket([0,1.5],one_two,3) == 1)
%! assert(bucket([1,1.5],one_two,3) == 1)

%!test "d=2, p=2, [*,0,0] -> [0,0]"
%!shared zero_one2
%! zero_one2=[0,0,0;1,1,1];
%! assert(bucket([0,0,0],zero_one2,2) == [0,0])
%! assert(bucket([1,0,0],zero_one2,2) == [0,0])

%!test "d=2, p=2, [*,0.6,0] -> [1,0]"
%! assert(bucket([0,0.6,0],zero_one2,2) == [1,0])
%! assert(bucket([1,0.6,0],zero_one2,2) == [1,0])

%!test "d=2, p=2, [*,0,0.6] -> [0,1]"
%! assert(bucket([0,0,0.6],zero_one2,2) == [0,1])
%! assert(bucket([1,0,0.6],zero_one2,2) == [0,1])

%!test "d=2, p=2, [*,1,1] -> [1,1]"
%! assert(bucket([0,1,1],zero_one2,2) == [1,1])
%! assert(bucket([1,1,1],zero_one2,2) == [1,1])

%!test "d=2, p=2, [*,1,1] -> [1,1]"
%! assert(bucket([0,1,1],zero_one2,2) == [1,1])
%! assert(bucket([1,1,1],zero_one2,2) == [1,1])