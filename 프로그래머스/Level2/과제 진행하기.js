function parseTime(time){
    const [hour, min] = time.split(":");
    return Number(hour) * 60 + Number(min)
}
function solution(plans) {
    var answer = [];
    var stack = []
    var newplans = plans.map((plansd) => ([plansd[0], parseTime(plansd[1]), plansd[2]]));
    newplans.sort((a, b) => a[1] - b[1]);

    for (var i = 0; i < newplans.length; i++){
        const [name, start, studytime] = newplans[i];
        if (stack.length > 0){
            const [prev_name, prev_start, prev_studytime] = stack.pop();

            var extra_time = start - prev_start;
            if(extra_time < prev_studytime){
                stack.push([prev_name, prev_start, prev_studytime - extra_time])
            }
            else {
                answer.push(prev_name); //정답 추가
                extra_time = extra_time - prev_studytime;
                while (stack.length > 0 && extra_time){
                    const [prev_name, prev_start, prev_studytime] = stack.pop();
                    if (extra_time < prev_studytime){
                        stack.push([prev_name, prev_start, prev_studytime - extra_time]);
                        break;
                    }
                    else {
                        answer.push(prev_name);
                        extra_time = extra_time - prev_studytime;
                    }
                }
            }

        }
        stack.push(newplans[i]);
    }

    stack.reverse();
    stack.map((a) => {answer.push(a[0])});

    return answer;
}