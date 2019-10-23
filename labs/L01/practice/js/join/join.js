function join(lst) {
    return lst.reduce((acc,cur) => acc.concat(cur), "");
}
exports.join = join;