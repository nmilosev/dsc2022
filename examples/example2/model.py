def add_vectors(v1, v2):
    return [sum(i) for i in zip(v1, v2)]
def mul_vector_number(v1, num):
    return [i * num for i in v1]
def score(input):
    if input[3] <= 0.800000011920929:
        var0 = [1.0, 0.0, 0.0]
    else:
        if input[0] <= 5.75:
            var0 = [0.0, 1.0, 0.0]
        else:
            if input[2] <= 4.950000047683716:
                if input[2] <= 4.8500001430511475:
                    var0 = [0.0, 1.0, 0.0]
                else:
                    if input[3] <= 1.649999976158142:
                        var0 = [0.0, 1.0, 0.0]
                    else:
                        var0 = [0.0, 0.0, 1.0]
            else:
                var0 = [0.0, 0.0, 1.0]
    if input[3] <= 0.75:
        var1 = [1.0, 0.0, 0.0]
    else:
        if input[2] <= 4.75:
            var1 = [0.0, 1.0, 0.0]
        else:
            if input[3] <= 1.550000011920929:
                if input[1] <= 2.9499999284744263:
                    var1 = [0.0, 0.0, 1.0]
                else:
                    var1 = [0.0, 1.0, 0.0]
            else:
                var1 = [0.0, 0.0, 1.0]
    if input[2] <= 4.75:
        if input[2] <= 2.350000023841858:
            var2 = [1.0, 0.0, 0.0]
        else:
            if input[0] <= 4.950000047683716:
                var2 = [0.0, 0.0, 1.0]
            else:
                var2 = [0.0, 1.0, 0.0]
    else:
        if input[2] <= 4.950000047683716:
            if input[1] <= 2.600000023841858:
                var2 = [0.0, 1.0, 0.0]
            else:
                var2 = [0.0, 0.0, 1.0]
        else:
            var2 = [0.0, 0.0, 1.0]
    if input[2] <= 2.350000023841858:
        var3 = [1.0, 0.0, 0.0]
    else:
        if input[2] <= 4.950000047683716:
            if input[3] <= 1.6500000357627869:
                var3 = [0.0, 1.0, 0.0]
            else:
                var3 = [0.0, 0.0, 1.0]
        else:
            var3 = [0.0, 0.0, 1.0]
    if input[2] <= 2.599999964237213:
        var4 = [1.0, 0.0, 0.0]
    else:
        if input[3] <= 1.6500000357627869:
            if input[3] <= 1.449999988079071:
                if input[1] <= 2.649999976158142:
                    if input[2] <= 5.0:
                        var4 = [0.0, 1.0, 0.0]
                    else:
                        var4 = [0.0, 0.0, 1.0]
                else:
                    var4 = [0.0, 1.0, 0.0]
            else:
                if input[2] <= 4.849999904632568:
                    var4 = [0.0, 1.0, 0.0]
                else:
                    var4 = [0.0, 0.0, 1.0]
        else:
            var4 = [0.0, 0.0, 1.0]
    if input[3] <= 0.800000011920929:
        var5 = [1.0, 0.0, 0.0]
    else:
        if input[3] <= 1.699999988079071:
            if input[3] <= 1.3499999642372131:
                var5 = [0.0, 1.0, 0.0]
            else:
                if input[2] <= 5.25:
                    var5 = [0.0, 1.0, 0.0]
                else:
                    var5 = [0.0, 0.0, 1.0]
        else:
            if input[0] <= 6.049999952316284:
                if input[1] <= 3.100000023841858:
                    var5 = [0.0, 0.0, 1.0]
                else:
                    var5 = [0.0, 1.0, 0.0]
            else:
                var5 = [0.0, 0.0, 1.0]
    if input[0] <= 5.450000047683716:
        if input[3] <= 0.800000011920929:
            var6 = [1.0, 0.0, 0.0]
        else:
            var6 = [0.0, 1.0, 0.0]
    else:
        if input[2] <= 4.950000047683716:
            if input[2] <= 2.600000023841858:
                var6 = [1.0, 0.0, 0.0]
            else:
                if input[2] <= 4.8500001430511475:
                    if input[3] <= 1.699999988079071:
                        var6 = [0.0, 1.0, 0.0]
                    else:
                        if input[0] <= 5.950000047683716:
                            var6 = [0.0, 1.0, 0.0]
                        else:
                            var6 = [0.0, 0.0, 1.0]
                else:
                    if input[3] <= 1.75:
                        var6 = [0.0, 1.0, 0.0]
                    else:
                        var6 = [0.0, 0.0, 1.0]
        else:
            var6 = [0.0, 0.0, 1.0]
    if input[2] <= 2.600000023841858:
        var7 = [1.0, 0.0, 0.0]
    else:
        if input[3] <= 1.6500000357627869:
            if input[2] <= 4.849999904632568:
                var7 = [0.0, 1.0, 0.0]
            else:
                var7 = [0.0, 0.0, 1.0]
        else:
            if input[2] <= 4.8500001430511475:
                if input[0] <= 5.950000047683716:
                    if input[2] <= 4.650000095367432:
                        var7 = [0.0, 0.0, 1.0]
                    else:
                        var7 = [0.0, 1.0, 0.0]
                else:
                    var7 = [0.0, 0.0, 1.0]
            else:
                var7 = [0.0, 0.0, 1.0]
    if input[2] <= 2.449999988079071:
        var8 = [1.0, 0.0, 0.0]
    else:
        if input[0] <= 5.75:
            if input[0] <= 4.950000047683716:
                var8 = [0.0, 0.0, 1.0]
            else:
                if input[3] <= 1.75:
                    var8 = [0.0, 1.0, 0.0]
                else:
                    var8 = [0.0, 0.0, 1.0]
        else:
            if input[2] <= 4.950000047683716:
                if input[1] <= 2.75:
                    if input[3] <= 1.649999976158142:
                        var8 = [0.0, 1.0, 0.0]
                    else:
                        var8 = [0.0, 0.0, 1.0]
                else:
                    var8 = [0.0, 1.0, 0.0]
            else:
                var8 = [0.0, 0.0, 1.0]
    if input[3] <= 0.800000011920929:
        var9 = [1.0, 0.0, 0.0]
    else:
        if input[0] <= 5.75:
            if input[3] <= 1.600000023841858:
                var9 = [0.0, 1.0, 0.0]
            else:
                var9 = [0.0, 0.0, 1.0]
        else:
            if input[0] <= 7.049999952316284:
                if input[2] <= 4.75:
                    var9 = [0.0, 1.0, 0.0]
                else:
                    if input[2] <= 5.0:
                        if input[0] <= 6.25:
                            var9 = [0.0, 0.0, 1.0]
                        else:
                            var9 = [0.0, 1.0, 0.0]
                    else:
                        var9 = [0.0, 0.0, 1.0]
            else:
                var9 = [0.0, 0.0, 1.0]
    return mul_vector_number(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(add_vectors(var0, var1), var2), var3), var4), var5), var6), var7), var8), var9), 0.1)

