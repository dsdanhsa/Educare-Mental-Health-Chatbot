
// function updateTime() {
//     var now = new Date();
//     var hours = now.getHours();
//     var minutes = now.getMinutes();
//     var seconds = now.getSeconds();
//     var timeString = hours + ':' + minutes;
//     document.getElementById('clock').textContent = timeString;
//   }
//   setInterval(updateTime, 1000);

// var running = false;
// document.getElementById("chatbot_toggle").onclick = function () {
// if (document.getElementById("chatbot").classList.contains("collapsed")) {
// document.getElementById("chatbot").classList.remove("collapsed")
// document.getElementById("chatbot_toggle").children[0].style.display = "none"
// document.getElementById("chatbot_toggle").children[1].style.display = ""
// setTimeout(addResponseMsg,1000,"Hi")
// }
// else {
// document.getElementById("chatbot").classList.add("collapsed")
// document.getElementById("chatbot_toggle").children[0].style.display = ""
// document.getElementById("chatbot_toggle").children[1].style.display = "none"
// }
// }

// const msgerForm = get(".msger-inputarea");
// const msgerInput = get(".msger-input");
// const msgerChat = get(".msger-chat");
// // Icons made by Freepik from www.flaticon.com
// const BOT_IMG = "static/img/mhcicon.png";
// const PERSON_IMG = "static/img/person.png";
// const BOT_NAME = "    Psychiatrist Bot";
// const PERSON_NAME = "You";
// msgerForm.addEventListener("submit", event => {
// event.preventDefault();
// const msgText = msgerInput.value;
// if (!msgText) return;
// appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
// msgerInput.value = "";
// botResponse(msgText);
// });
// function appendMessage(name, img, side, text) {
// //   Simple solution for small apps
// const msgHTML = `
// <div class="msg ${side}-msg">
// <div class="msg-img" style="background-image: url(${img})"></div>
// <div class="msg-bubble">
// <div class="msg-info">
// <div class="msg-info-name">${name}</div>
// <div class="msg-info-time">${formatDate(new Date())}</div>
// </div>
// <div class="msg-text">${text}</div>
// </div>
// </div>
// `;
// msgerChat.insertAdjacentHTML("beforeend", msgHTML);
// msgerChat.scrollTop += 500;
// }
// function botResponse(rawText) {
// // Bot Response
// $.get("/get", { msg: rawText }).done(function (data) {
// console.log(rawText);
// console.log(data);
// const msgText = data;
// appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
// });
// }
// // Utils
// function get(selector, root = document) {
// return root.querySelector(selector);
// }
// function formatDate(date) {
// const h = "0" + date.getHours();
// const m = "0" + date.getMinutes();
// return `${h.slice(-2)}:${m.slice(-2)}`;
// }

$(document).ready(function() {
  $('.msger-send-btn').click(function(e) {
    e.preventDefault(); // Ngăn chặn form gửi đi mặc định
    let userText = $('#textInput').val().trim();
    if (userText === "") return;

    // Xóa nội dung trong input sau khi gửi
    $('#textInput').val('');

    // Thêm tin nhắn của người dùng vào khung chat
    $('.msger-chat').append(`
      <div class="msg right-msg">
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">Bạn</div>
          </div>
          <div class="msg-text">${userText}</div>
        </div>
      </div>
    `);

    // Cuộn xuống cuối khung chat
    $('.msger-chat').scrollTop($('.msger-chat')[0].scrollHeight);

    // Gửi tin nhắn đến server qua AJAX
    $.ajax({
      url: '{% url "get_bot_response" %}', // Sử dụng tên URL của Django
      type: 'GET', // Kiểu yêu cầu HTTP
      data: { 'msg': userText },
      dataType: 'json',
      success: function(data) {
        // Kiểm tra và lấy nội dung từ `data.response`
        const botResponse = data.response || "Xin lỗi, đã xảy ra lỗi khi lấy phản hồi.";

        // Hiển thị phản hồi từ bot với ảnh từ thư mục static
        $('.msger-chat').append(`
          <div class="msg left-msg">
            <div class="msg-img" style="background-image: url('{% static "img/mhcicon.png" %}')"></div>
            <div class="msg-bubble">
              <div class="msg-info">
                <div class="msg-info-name">EduCare Bot</div>
                <div class="msg-info-time">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
              </div>
              <div class="msg-text">${botResponse}</div>
            </div>
          </div>
        `);
        
        // Cuộn xuống cuối khung chat sau khi bot trả lời
        $('.msger-chat').scrollTop($('.msger-chat')[0].scrollHeight);
      },
      error: function() {
        // Xử lý khi có lỗi
        $('.msger-chat').append(`
          <div class="msg left-msg">
            <div class="msg-img" style="background-image: url('{% static "img/mhcicon.png" %}')"></div>
            <div class="msg-bubble">
              <div class="msg-info">
                <div class="msg-info-name">EduCare Bot</div>
                <div class="msg-info-time">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
              </div>
              <div class="msg-text">Đã xảy ra lỗi.</div>
            </div>
          </div>
        `);
        
        // Cuộn xuống cuối khung chat
        $('.msger-chat').scrollTop($('.msger-chat')[0].scrollHeight);
      }
    });
  });

  // Gửi tin nhắn khi nhấn Enter
  $('#textInput').keypress(function(e) {
    if (e.which === 13) {
      $('.msger-send-btn').click();
    }
  });
});
