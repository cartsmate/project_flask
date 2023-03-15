function sum_score(){
    var total_score = 0
    for (let i = 0; i < score_list.length; i++) {
        total_score = total_score + Number(document.getElementById(score_list[i]).value)
    }
    document.getElementById("score").value = total_score
    document.getElementById("value_score").innerHTML = total_score + "%"
}