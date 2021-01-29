import './profile.css'
import profilePicture from '../../media/anime.jpeg'
import {ColorExtractor} from "react-color-extractor";
import {useState} from "react";

function Profile() {
  const [commonColor, setCommonColor] = useState()

  return <div className="profile">
	<div className="skew-block" style={{backgroundColor: `${commonColor}`, opacity: '0.4'}}/>
	<div className="skew-block-bottom" style={{backgroundColor: `${commonColor}`, opacity: '0.3'}}/>
	<ColorExtractor
		src={profilePicture}
		getColors={colors => setCommonColor(colors[0])}
	/>
	<div className="profile-block">
	  <div className="profile-title">
		<h1><span>Профіль |</span> Максим Примаченко
		  <div style={{
			height: '5px',
			width: '50%',
			position: 'absolute',
			borderRadius: '9999px',
			bottom: '-20px',
			left: '0',
			backgroundColor: `${commonColor}`
		  }}/></h1>

	  </div>
	  <div className="img-info-wrapper">
		<div className="profile-img">
		  <img src={profilePicture}/>
		</div>
		<div className="profile-info">
		  <p>група кн-215</p>
		  <p>студентський кн-215</p>
		  <p>інфа кн-215</p>
		  <p>інфа лфлф</p>
		  <p>інфа лаала</p>
		</div>
	  </div>
	</div>
  </div>

}

export default Profile;