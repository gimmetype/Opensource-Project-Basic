const $c = document.querySelector("canvas");
const ctx = $c.getContext(`2d`);


const product = [
  "한식", "중식", "돈까스·일식", "카페·디저트", "아시안·양식", "패스트푸드", "분식", "고기 요리", "기타",
];

const colors = ["#F6F1F1", "#AFD3E2", "#19A7CE", "#146C94"];

const newMake = () => {
    const [cw, ch] = [$c.width / 2, $c.height / 2];
    const arc = Math.PI / (product.length / 2);

    for (let i = 0; i < product.length; i++) {
      ctx.beginPath();
      ctx.fillStyle = colors[i % (colors.length -1)];
      ctx.moveTo(cw, ch);
      ctx.arc(cw, ch, cw, arc * (i - 1), arc * i);
      ctx.fill();
      ctx.closePath();
    }

    ctx.fillStyle = "#394867";
    ctx.font = "18px Pretendard";
    ctx.textAlign = "center";

    for (let i = 0; i < product.length; i++) {
      const angle = (arc * i) + (arc / 2);

      ctx.save()  ;

      ctx.translate(
        cw + Math.cos(angle) * (cw - 50),
        ch + Math.sin(angle) * (ch - 50),
      );

      ctx.rotate(angle + Math.PI / 2);

      product[i].split(" ").forEach((text, j) => {
        ctx.fillText(text, 0, 30 * j);
      });

      ctx.restore();
    }
}

const rotate = () => {
  $c.style.transform = `initial`;
  $c.style.transition = `initial`;

  setTimeout(() => {

    const ran = Math.floor(Math.random() * product.length);

    const arc = 360 / product.length;
    const rotate = (ran * arc) + 3600 + (arc * 3) - (arc/4);

    $c.style.transform = `rotate(-${rotate}deg)`;
    $c.style.transition = `1.5s`;

    setTimeout(() => alert(`오늘 ${product[ran]} 어떠신가요?`), 2000);
  }, 1);
};

newMake();