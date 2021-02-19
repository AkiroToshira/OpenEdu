import React, {useState} from "react";
import {Link} from "react-router-dom";
import {motion, AnimatePresence} from "framer-motion";

const backdrop = {
  visible: {opacity: 1},
  hidden: {opacity: 0},
};

const backdrop1 = {
  position: "fixed",
  top: "0",
  left: "0",
  width: "100%",
  height: "100%",
  // background: "rgba(0,0,0,0.5)",
  zIndex: "1",
}
const modal1 = {
  maxWidth: "400px",
  margin: "0 auto",
  padding: "40px 20px",
  backgroundColor: "red",
  borderRadius: "6px",
  textAlign: "center",
}

const Popup = ({showPopup}) => {
  return (
	  <AnimatePresence>
		{showPopup && (
			<motion.div
				style={backdrop1}
				variants={backdrop}
				initial="hidden"
				animate="visible"
				exit="hidden"
			>
			  <motion.div
				  style={modal1}
				  initial={{scale: 0, y: 100}}
				  animate={{scale: 2, y: 100}}
				  transition={{
					type: "spring",
					stiffness: 150,
					damping: 10
				  }}>
				dsdsd
			  </motion.div>

			</motion.div>

		)}
	  </AnimatePresence>
  );
};

export default Popup;
