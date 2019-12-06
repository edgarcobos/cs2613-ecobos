leaf=imread("leaf.jpg");
monoleaf=monochrome(leaf);
smoothed = smooth(monoleaf,5);
ng =normgrad(smoothed);
[rows, cols] = threshold(ng, 8);

clf
hold on;
imshow(leaf);
plot(cols,rows,".","markersize",1);