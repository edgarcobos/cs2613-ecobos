function S=smooth(in, side=3)
    S = conv2(in,ones(side,side)/(side^2),"same");
endfunction

%!test
%! A = [0,0,0,1;
%!      1,1,0,0;
%!      1,1,0,1;
%!      1,1,1,0];
%! B= [0.50, 0.25, 0.25, 0.25;
%!     1.00, 0.50, 0.25, 0.25;
%!     1.00, 0.75, 0.50, 0.25;
%!     0.50, 0.50, 0.25, 0.00];
%! assert(smooth(A,2),B,eps);

%!demo
%! paris=imread("paris.jpg");
%! monoparis=monochrome(paris,[1/3,1/3,1/3]);
%! imshow(monoparis,[])
%! pause(1);
%! imshow(smooth(monoparis),[])
%! pause(1);
%! imshow(smooth(monoparis,10),[])
%! pause(1);
%! imshow(smooth(monoparis,20),[])