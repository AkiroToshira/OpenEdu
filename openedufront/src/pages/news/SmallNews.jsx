import { manageDate, manageText, manageTitle } from "../../helpers/manage";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useRef, useState } from "react";
import BigModal from "../../components/modal/bigModal";
import axios from "axios";
import { url } from "../../helpers/utils";

function SmallNews() {
  const dispatch = useDispatch();
  const smallNews = useSelector((state) => state.news);

  if (!smallNews.loading) {
    return (
      <section className="small-news">
        <h1 className="upcoming-news">Найсвіжіші Новини</h1>
        <div className="small-news-list">
          {smallNews.data.smallNews.map((el, i) => (
            <OneNews data={smallNews.data.smallNews[i]} key={i} />
          ))}
        </div>
      </section>
    );
  } else {
    return (
      <section className="small-news">
        <div className="small-news-list">
          {[1, 2, 3, 4, 5].map((el) => {
            return (
              <div className={"small-news-skeleton one-news"} key={el}>
                <div className="news-skew" />
              </div>
            );
          })}
        </div>
      </section>
    );
  }
}

function OneNews(el) {
  const [smallNewsById, setSmallNewsById] = useState(null);

  const news = useSelector((state) => state.news);
  const auth = useSelector((state) => state.auth);

  const { creation_date, name, mini_description, id } = el.data;

  const modalRef = useRef();

  const handleSmallNewsById = async (id) => {
    await axios
      .get(`${url}/news/${id}`, {
        headers: {
          Authorization: "JWT " + auth.token.access,
        },
      })
      .then((res) => {
        setSmallNewsById(res.data);
      });
  };

  return (
    <div className="one-news">
      {smallNewsById && (
        <BigModal ref={modalRef}>
          <div className="popup-container">
            <span className="creation_date_expand">{smallNewsById.creation_date}</span>
            <span className="name_expand">{smallNewsById.name.toUpperCase()}</span>
            <span className="description_expand">{smallNewsById.description.toUpperCase()}</span>
          </div>
          <div className="right-photo">
          </div>
        </BigModal>
      )}
      <div className="wrapper-img-date">
        <div className="small-news-date">
          <span className="date">{manageDate(creation_date)[0]}</span>
          <span className="month">{manageDate(creation_date)[1]}</span>
        </div>
        <div className="small-news-photo" />
      </div>
      <div className="small-news-text">
        <div className="small-news-title">{manageTitle(name)}</div>
        <div className="small-news-description">
          {manageText(mini_description)}
        </div>
        <div
          className="small-news-check-detailed"
          onClick={() => {
            handleSmallNewsById(id).then(() => modalRef.current.open());
          }}
        >
          Більше про новину
        </div>
      </div>
    </div>
  );
}

export default SmallNews;
