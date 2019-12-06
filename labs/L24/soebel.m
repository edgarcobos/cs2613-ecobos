function [Gx,Gy]=soebel(in)
  mask = [1, 0, -1;
                2,0,-2;
                1,0,-1];
  Gx = conv2(in, mask, "valid");
  Gy = conv2(in, mask', "valid");
endfunction

%!demo
%! leaf=imread("leaf.jpg");
%! monoleaf=monochrome(leaf);
%! [Dx, Dy] = soebel(monoleaf);
%! ns = norm2(Dx,Dy);
%! [rows,cols] = threshold(ns,150);
%! clf
%! hold on
%! imshow(leaf);
%! plot(cols,rows,".","markersize",1);