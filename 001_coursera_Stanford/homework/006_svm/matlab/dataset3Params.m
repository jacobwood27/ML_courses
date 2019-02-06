function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%


v = [ 0.01, 0.03, 0.1, 0.3, 1, 3 10 30];
[Cv,sv] = meshgrid(v,v);
j=nan(size(Cv));
for ii=1:numel(v)
    for kk=1:numel(v)
        Ct=Cv(ii,kk);
        st=sv(ii,kk);
        
        model = svmTrain(X, y, Ct, @(x1, x2)gaussianKernel(x1, x2, st));
        pred = svmPredict(model, Xval);
        
        j(ii,kk)=mean(double(pred ~= yval));
        
    end
end

[~,idx]=min(j(:));
[row,col]=ind2sub(size(j),idx);
C=v(col);
sigma=v(row);

% figure
% contourf(1:numel(v),1:numel(v),j,[0.04 0.06 0.1 0.15 0.2])


% =========================================================================

end
