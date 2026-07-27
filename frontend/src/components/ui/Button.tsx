import type { ButtonHTMLAttributes, ReactNode } from "react";

import { cn } from "../../lib/utils";
import { buttonSizes, buttonVariants } from "./buttonVariants";

type ButtonVariant =
  | "primary"
  | "secondary"
  | "danger"
  | "ghost";

type ButtonSize =
  | "sm"
  | "md"
  | "lg";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  variant?: ButtonVariant;
  size?: ButtonSize;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  loading?: boolean;
}

function Button({
  children,
  variant = "primary",
  size = "md",
  className,
  leftIcon,
  rightIcon,
  loading = false,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      disabled={disabled || loading}
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-lg font-medium transition-all duration-200",
        "focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]",
        "disabled:cursor-not-allowed disabled:opacity-50",
        buttonVariants[variant],
        buttonSizes[size],
        className
      )}
      {...props}
    >
      {leftIcon}

      {loading ? "Loading..." : children}

      {rightIcon}
    </button>
  );
}

export default Button;