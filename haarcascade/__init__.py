"""Detection with Haar cascade and filtering with Non-Maxima Supression (NMS)."""

import cv2


class Detector(cv2.CascadeClassifier):
    """Extend the opencv haar-cascade detector, by adding the method detectAndFilter."""
    
    def detectAndFilter(self, 
                        image, 
                        scaleFactor,
                        minSize, maxSize, 
                        score_threshold, 
                        overlap_threshold, 
                        nObjects=float("inf")):
        """Detect object using trained cascade and filter overlapping detections with NMS."""
        # Initial detection
        bboxes, rejectLevel, levelWeights = self.detectMultiScale3(image,
                                                                   scaleFactor,
                                                                   minNeighbors = 1,
                                                                   minSize = minSize,
                                                                   maxSize = maxSize,
                                                                   outputRejectLevels = True)
        # BBoxes formatting and NMS
        scores = levelWeights[:,0]
        indexes = cv2.dnn.NMSBoxes(bboxes.tolist(), scores, score_threshold, overlap_threshold)
        
        # final list of hits
        nBoxes = len(indexes)
        finalScores = [None] * nBoxes 
        finalBoxes  = [None] * nBoxes
        
        for i, index in enumerate(indexes[:,0]):
            finalBoxes [i] = bboxes[index].tolist()
            finalScores[i] = scores[index]
        
        # Return up to nObjects if mentioned
        if nObjects != float("inf"):
            finalBoxes  = finalBoxes[:nObjects]
            finalScores = finalScores[:nObjects]
        
        return finalBoxes, finalScores