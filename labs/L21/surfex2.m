a = [4;4];
beta = 7.5;
range = [-4:0.1:8];
[X Y] = meshgrid(range,range);

%f=@(x,y)(delta(beta,a,[x;y]));
f=@(x,y)(beta*(a(1)*x+a(2)*y) - (beta-1) * (x^2+y^2));

tic();
Z=arrayfun(f,X,Y);
toc()

surf(X,Y,Z);
