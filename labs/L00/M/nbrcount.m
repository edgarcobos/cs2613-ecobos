function out = nbrcount(img)
  mask = [1, 1, 1;
                 1, 0, 1;
                 1, 1, 1];
  out = conv2(img, mask, "same");
endfunction

%!test
%! A=       [1,0,0;
%!           0,0,0;
%!           0,0,1;
%!           1,0,0];
%! counts = [0,1,0; 1,2,1; 1,2,0; 0,2,1]
%! assert(nbrcount(A) == counts)