import './modal.css'
import {AnimatePresence, motion} from "framer-motion";
import {forwardRef, useImperativeHandle, useState} from "react";

function SmallModal(props, ref) {

  const [open, setOpen] = useState(false)

  useImperativeHandle(ref, () => {
    return {
      add: () => setOpen(true),
      end: () => setOpen(false)
    }
  })

  return <AnimatePresence>
    {open && <>
      <motion.div
          initial={{
            opacity: 0,
          }}
          animate={{
            opacity: 1,
            transition: {
              duration: .3
            }
          }}
          exit={{
            opacity: 0,
          }}
          onClick={() => setOpen(p => !p)}
          className="my-modal-backdrop"/>
      <motion.div
          initial={{
            scale: 0
          }}

          animate={{
            scale: 1,
            transition: {
              duration: .3
            }
          }}
          exit={{
            scale: 1.1,
          }}

          className="my-modal-content-wrapper small-modal">
        <motion.div className="my-modal-content">{props.children}</motion.div>
      </motion.div>
    </>}
  </AnimatePresence>
}

export default  forwardRef(SmallModal)