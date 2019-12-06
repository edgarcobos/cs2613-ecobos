leaf=imread("leaf.jpg");
monoleaf=monochrome(leaf);
ng =normgrad(monoleaf);
[rows, cols] = threshold(ng, 8 );

clf
hold on;
imshow(leaf);
plot(cols,rows,".","markersize",1);