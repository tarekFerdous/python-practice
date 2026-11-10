/* Reusable quiz component.
   Usage: <div class="quiz" id="q1"></div>
          <script src="../assets/quiz.js"></script>
          <script>Quiz.render('q1', [{ q: 'Question?', options: ['a','b','c','d'], answer: 2, why: 'Explanation.' }]);</script>
   `answer` is the 0-based index of the correct option. One attempt per question; the explanation shows after answering. */
window.Quiz = {
  render: function (id, questions) {
    var root = document.getElementById(id), score = 0, answered = 0;
    var tally = document.createElement('p');
    tally.className = 'quiz-score';
    questions.forEach(function (item, qi) {
      var wrap = document.createElement('div');
      wrap.className = 'quiz-q';
      var q = document.createElement('p');
      q.className = 'q';
      q.innerHTML = (qi + 1) + '. ' + item.q;   // question text is authored by the teacher (may contain <code>)
      wrap.appendChild(q);
      var buttons = item.options.map(function (opt, oi) {
        var b = document.createElement('button');
        b.type = 'button';
        b.innerHTML = opt;
        b.addEventListener('click', function () {
          buttons.forEach(function (x) { x.disabled = true; });
          buttons[item.answer].classList.add('right');
          if (oi === item.answer) score++; else b.classList.add('wrong');
          answered++;
          wrap.classList.add('done');
          tally.textContent = 'Score: ' + score + ' / ' + answered + (answered === questions.length ? ' (done; anything you missed, ask your teacher why)' : '');
        });
        wrap.appendChild(b);
        return b;
      });
      var why = document.createElement('p');
      why.className = 'why';
      why.innerHTML = item.why;
      wrap.appendChild(why);
      root.appendChild(wrap);
    });
    root.appendChild(tally);
  }
};
