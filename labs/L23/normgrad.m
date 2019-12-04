function normimg = normgrad(img)
  [Dx, Dy] = gradient(img);
  normimg = sqrt(Dx.^2 + Dy.^2);
endfunction

%!demo
%! owl=imread("owl.jpg");
%! monowl=monochrome(owl);
%! ng = normgrad(monowl);
%! imshow(ng*2, [0,20]);