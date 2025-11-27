const editor = new window.tiptap.Core.Editor({
    element: document.querySelector('#editor'),
    extensions: [
        window.tiptap.StarterKit,
        window.tiptap.Image,
    ],
    content: "<p>Escreva sua notícia aqui...</p>",
    onUpdate({ editor }) {
        document.querySelector('input[name=conteudo]').value = editor.getHTML();
    },
});

// ==== BOTÕES ====
function cmd(action) {
    editor.chain().focus()[`toggle${action.charAt(0).toUpperCase() + action.slice(1)}`]().run();
}

function header(level) {
    editor.chain().focus().toggleHeading({ level }).run();
}

function list(type) {
    if (type === "bullet") editor.chain().focus().toggleBulletList().run();
    else editor.chain().focus().toggleOrderedList().run();
}

function quote() {
    editor.chain().focus().toggleBlockquote().run();
}

function addLink() {
    const url = prompt("Digite a URL:");
    if (url) editor.chain().focus().extendMarkRange('link').setLink({ href: url }).run();
}

// ==== UPLOAD REAL DE IMAGEM ====
function uploadImage() {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";

    input.onchange = async () => {
        const file = input.files[0];
        const formData = new FormData();
        formData.append("image", file);

        const response = await fetch("{% url 'upload_imagem' %}", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": "{{ csrf_token }}",
            }
        });

        const data = await response.json();

        if (data.url) {
            editor.chain().focus().setImage({ src: data.url }).run();
        }
    };

    input.click();
}