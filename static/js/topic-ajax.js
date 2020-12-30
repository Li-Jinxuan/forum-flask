var apiReplyAdd = function(form, callback) {
  var path = '/reply/add'
  ajax('POST', path, form, callback)
}

var replyTemplate = function(reply) {
  var t = `
  <div class='cell reply_area reply_item'>
      <div class='author_content'>
          <div class='user_info'>
              <a class='dark reply_author'>
                  ${reply.username}
              </a>
              <a class="reply_time">
                  ${document.querySelectorAll(".reply_time").length + 1}楼 •
                  <span class="gua-time" id="${reply.created_time}"></span>
              </a>
          </div>
          <div class='user_action'>
              <span>
                  <i class="fa up_btn
                    fa-thumbs-o-up
                    invisible" title="喜欢"></i>
                  <span class="up-count">
                  </span>
              </span>
          </div>
      </div>
      <div class='reply_content from-leiwei1991'>
          <div class="markdown-text">${reply.content}</div>

      </div>
  </div>
    `
  return t
}

var insertReply = function(reply) {
  var replyCell = replyTemplate(reply)
  // 插入 reply-list
  var replyList = e('#id-reply-list')
  replyList.insertAdjacentHTML('beforeend', replyCell)
}

var bindEventReplyAdd = function() {
  var b = e('#id-button-add')
  // 注意, 第二个参数可以直接给出定义函数
  b.addEventListener('click', function() {
    var input = e('#id-input-reply')
    var content = input.value
    log('click add', content)
    var topicId = e('#id-topicId').value
    var form = {
      content: content,
      topic_id: topicId
    }
    log("aaaaa", form)
    apiReplyAdd(form, function(r) {
      // 收到返回的数据, 插入到页面中
      var reply = JSON.parse(r)
      log("bbbbb", reply)
      insertReply(reply)
      input.value = ""
      e('.col_fade').innerHTML = document.querySelectorAll(".reply_time").length + " 回复"

      contentDiv = document.querySelectorAll('.markdown-text')[document.querySelectorAll('.markdown-text').length-1]
      contentDiv.innerHTML = marked(contentDiv.textContent)
      Prism.plugins.autoloader.languages_path = 'https://cdn.bootcss.com/prism/1.13.0/components/'
    })


//    markContents()
//    highlight()

  })
}

var bindEvents = function() {
  bindEventReplyAdd()
}

var __main = function() {
  bindEvents()
}

__main()
