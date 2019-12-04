function out=findclass(v, k, data, fun=@nearest)
    selection=fun(v,k,data);
    out = mode(data(selection,1));
endfunction

%!test
%! v = [0,1,1];
%! data = [0,0,0; 0,0,1; 0,1,0; 1,1,1];
%! assert(findclass(v,1,data) == 1)
%! assert(findclass(v,3,data) == 0)