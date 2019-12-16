function out = isolated(img)
  out = nbrcount(img) - img;
  idx = find(out > 0);
  out(idx) = 0;
  idx = find(out < 0);
  out(idx) = 1;
endfunction

%!test
%! A= [1,0,0; 0,0,0; 0,0,1; 1,0,0];
%! assert(isolated(A) == A)

%!test
%! A=[1,0,0;
%!    0,0,0;
%!    0,1,1;
%!    1,0,1];
%! assert(isolated(A) == [1,0,0; 0,0,0; 0,0,0;0,0,0])