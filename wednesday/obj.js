const stling = "2.64"

const floatParser = (st, v, c) => {
    let fnl = c
    switch (st) {
        case "-":
            fnl * -1
            break;
        case ".":
            break;
        default:
            fnl > 0 ? fnl = fnl + st / 10**v : fnl = fnl - st / 10**v
            break;
            
    }
    return fnl
}

let computedNum = 0
for(s of stling) {
    index = stling.indexOf("-") === 0 ? stling.indexOf(s) - 1 : stling.indexOf(s)
    computedNum = floatParser(s, index, computedNum)
    computedNum > 0 & stling.indexOf("-") === 0 ? computedNum = computedNum * -1 : console.log("")
    console.log(computedNum)
}