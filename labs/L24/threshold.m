function [rows, cols] = threshold(in, lower=100)
  [rows,cols] = find(in > lower);
endfunction

%!test
%! A=[1,2,3; 4,5,6];
%!  [rows,cols]=threshold(A,4);
%!  assert(rows==[2;2]);
%!  assert(cols==[2;3]);

%!demo
%! leaf=imread("leaf.jpg");
%! monoleaf=monochrome(leaf);
%! [rows, cols] = threshold(monoleaf,200);
%! clf
%! hold on;
%! imshow(leaf);
%! plot(cols,rows,".","markersize",1);