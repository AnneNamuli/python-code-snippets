def arithGeo(arr) {
    var minRatio = 1/0,
        maxRatio = -1/0,
        minDiff  = 1/0,
        maxDiff  = -1/0,
        epsilon  = 0.000001,
        i,
        ratio,
        diff;

    if (arr.length <= 2) {
        return;
    }

    for (i = 1; i < arr.length; ++i) {
        diff  = arr[i] - arr[i - 1];
        ratio = arr[i] / arr[i - 1];
        minDiff  = Math.min(diff, minDiff);
        maxDiff  = Math.max(diff, maxDiff);
        minRatio = Math.min(ratio, minRatio);
        maxRatio = Math.max(ratio, maxRatio);
    }

    if (Math.abs(minDiff - maxDiff) < epsilon) {
        return "Arithmetic";
    }

    if (Math.abs(minRatio - maxRatio) < epsilon) {
        return "Geometric";
    }

    return;