import '../class.css'

function ClassStudent() {
  return (
	  <div className="container">
		<div className="first-section">

		  {/*{% for i in get_chapter %}*/}
		  <div className="col">
			<div className="title">
			  {/*<span>{{i.name}}</span>*/}
			</div>
			<div className="description">
			  {/*<span>{{i.description}}</span>*/}
			</div>
			<div className="title pdf">
			  {/*<a href="{{ i.document.url }}" download>{{i.document.name}}</a>*/}
			  {/*<img src="../../media/page/pdf.svg" alt="" className="user-png">*/}
			</div>
		  </div>
		  {/*{% endfor %}*/}

		</div>
		<div className="second-section">
		  <div className="col col-teacher-info">
			<div className="teacher-img" style={{margin: '0 auto'}}></div>
			<div className="whois">
			  <span>Викладач:</span>
			  <span>Мочурад Л. І.</span>
			</div>
			{/*<div className="teacher-info"><p>{{get_lesson.description}}</p></div>*/}
		  </div>
		</div>
	  </div>
  );
}


export default ClassStudent;