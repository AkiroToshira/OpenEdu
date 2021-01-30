

function Editchapter() {
    return <div className="modal-body">
        <form encType="multipart/form-data" action="" method="post">
            {/*{% csrf_token %}*/}
            {/*{{form.as_p}}*/}
            <div className="modal-footer">
                <button type="submit" name="button">Edit</button>
            </div>
        </form>
    </div>
}

export default Editchapter



