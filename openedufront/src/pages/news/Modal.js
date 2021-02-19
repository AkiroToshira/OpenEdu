import React, { useState } from "react";
import { Link } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";

const backdrop = {
  visible: { opacity: 1 },
  hidden: { opacity: 0 },
};

const modal = {
  hidden: {
    y: "-100vh",
    opacity: 0,
  },
  visible: {
    y: "100px",
    opacity: 1,
    transition: { delay: 0.5 },
  },
};

const backdrop1 = {
  position: "fixed",
  top: "0",
  left: "0",
  width: "100%",
  height: "100%",
  background: "rgba(0,0,0,0.5)",
  zIndex: "1",
}
const modal1 = {
  maxWidth: "400px",
  margin: "0 auto",
  padding: "40px 20px",
  backgroundColor: "white",
  borderRadius: "6px",
  textAlign: "center",
}


const modalP1 = {
  color: "#444",
  fontWeight: "bold",
}

const closeModal = (setShowModal) => {
  setShowModal(p => !p)
}

const Modal = ({ showModal, setShowModal}) => {
  return (
    <AnimatePresence>
      {showModal && (
        <motion.div
          style={backdrop1}
          variants={backdrop}
          initial="hidden"
          animate="visible"
          exit="hidden"
        >
          <motion.div
            style={modal1}
            variants={modal}

          >
            <div style={modalP1}>
              Some texts...
              <span onClick={() => closeModal(setShowModal)}>X</span>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default Modal;
