## usage: scale_layers(array, weights)
##
## multiply each layer of a 3D array by the corresponding weight
function out = scale_layers(array, weights)
  out = array .* reshape(weights, [1,1,3]);
endfunction

%!test
%! onez = ones(3,3);
%! A=cat(3,onez, 2*onez, 3*onez);
%! B=cat(3,onez, 6*onez, 15*onez);
%! assert(scale_layers(A,[1;3;5]),B)